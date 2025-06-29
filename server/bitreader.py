#bitreader.py
class BitReader:
    def __init__(self, data: bytes):
        self.data = data
        self.bit_index = 0

    def read_bits(self, count: int) -> int:
        result = 0
        for _ in range(count):
            byte_index = self.bit_index // 8
            bit_offset = 7 - (self.bit_index % 8)
            if byte_index >= len(self.data):
                raise ValueError("Not enough data to read")
            bit = (self.data[byte_index] >> bit_offset) & 1
            result = (result << 1) | bit
            self.bit_index += 1
        return result

    def read_bit(self) -> int:
        return self.read_bits(1)

    def remaining_bits(self) -> int:
        """
        Return the number of bits remaining in the data buffer.
        """
        total_bits = len(self.data) * 8
        return max(0, total_bits - self.bit_index)

    def read_signed_bits(self, count: int) -> int:
            """
            Read `count` bits and return as a signed integer (two's complement).
            """
            val = self.read_bits(count)
            sign_bit = 1 << (count - 1)
            # if sign_bit is set, flip and subtract to get negative

            return (val ^ sign_bit) - sign_bit

    def align_to_byte(self):
        remainder = self.bit_index % 8
        if remainder != 0:
            self.bit_index += (8 - remainder)

    def read_string(self) -> str:
        self.align_to_byte()
        length = self.read_bits(16)
        result_bytes = bytearray()
        for _ in range(length):
            result_bytes.append(self.read_bits(8))
        try:
            return result_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return result_bytes.decode('latin1')

    def read_method_4(self) -> int:
        n = self.read_bits(4)
        n = (n + 1) << 1
        return self.read_bits(n)

    def read_method_393(self) -> int:
        return self.read_bits(8)

    def read_method_6(self, bit_count: int) -> int:
        return self.read_bits(bit_count)


    def read_method_9(self) -> int:
        # 1) Read the 4-bit unary length prefix
        prefix = self.read_bits(4)
        # length in bits = 2*(prefix + 1)
        n_bits = (prefix + 1) * 2

        # 2) Read the unsigned integer payload
        raw = self.read_bits(n_bits)
        return raw

    def read_int24(self) -> int:
        # 1) sign
        sign = self.read_bits(1)
        # 2) magnitude
        mag  = self.read_method_9()
        return -mag if sign else mag


