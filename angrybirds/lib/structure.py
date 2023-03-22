#!/usr/bin/env python3
""" Structure Class """
import struct


class StructField:
    '''
    Descriptor representing a simple structure field
    '''

    def __init__(self, fmt, offset):
        self.fmt = fmt
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.fmt, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r


class NestedStruct:
    '''
    Descriptor representing a nested structure
    '''

    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:self.offset + self.struct_type.struct_size]
            result = self.struct_type(data)
            # Save resulting structure back on instance to avoid
            # further recomputation of this step
            setattr(instance, self.name, result)
            return result


class StructureMeta(type):
    '''
    Metaclass that automatically creates StructField descriptors
    '''

    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for fmt, fieldname in fields:
            if isinstance(fmt, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, fmt, offset))
                offset += fmt.struct_size
            else:
                if fmt.startswith(('<', '>', '!', '@')):
                    byte_order = fmt[0]
                    fmt = fmt[1:]
                fmt = byte_order + fmt
                setattr(self, fieldname, StructField(fmt, offset))
                offset += struct.calcsize(fmt)
        setattr(self, 'struct_size', offset)


class Structure(metaclass=StructureMeta):
    '''
    Class creates Structure
    '''

    def __init__(self, bytedata):
        self._buffer = bytedata

    def encode_fmt(self, data):
        """[Recursive computing structure coding format]

        Arguments:
            data {[Structure]} -- [Structure]

        Returns:
            [str] -- [data format]
        """
        data = data if data else self
        data_fmt = ''
        fields = getattr(data, '_fields_', [])
        for fmt, fieldname in fields:
            if isinstance(fmt, StructureMeta):
                data_fmt += self.encode_fmt(fmt)
            else:
                data_fmt += fmt
        return data_fmt

    def encode_data(self):
        """[Recursive computing structure coding bytes stream]

        Arguments:
            data {[Structure]} -- [Structure]

        Keyword Arguments:
            byte_order {str} -- [byte order] (default: {'<'})

        Returns:
            [bytesarrary] -- [bytes stream]
        """

        def _encode_data(data, byte_order='<'):
            send_buf = b''
            if isinstance(data, list):
                if not data:
                    return send_buf
                for i in range(len(data)):
                    send_buf += _encode_data(data[i], byte_order)
                return send_buf
            fields = getattr(data, '_fields_', [])
            for fmt, fieldname in fields:
                if isinstance(fmt, StructureMeta):
                    sub_data = getattr(data, fieldname)
                    send_buf += _encode_data(sub_data, byte_order)
                elif isinstance(fmt, str):
                    if fmt.startswith(('<', '>', '!', '@')):
                        byte_order = fmt[0]
                        fmt = fmt[1:]
                    fmt = byte_order + fmt
                    send_buf += struct.pack(fmt, getattr(data, fieldname))
                else:
                    print(fmt)
                    break
            return send_buf

        return _encode_data(self)


class SizedRecord:

    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)

    def unpack_num(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            num = s.unpack_from(self._buffer)[0]
            return s.size, num

    def iter_as(self, code, num):
        if isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer[0:num * size]), size):
                data = self._buffer[off:off + size]
                yield code(data)
