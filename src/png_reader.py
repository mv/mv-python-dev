###
### Ref:
###     https://realpython.com/read-write-files-python/#creating-your-own-context-manager
###

class PngReader():

    def __init__(self, pathname):
        # Ensure the file has the right extension
        if not pathname.endswith('.png'):
            raise NameError("File must have a '.png' extension")

        self.fh = None
        self.pathname = pathname


    # Every .png file must contain this magic header.
    _expected_magic = b'\x89PNG\r\n\x1a\n'

    def __enter__(self):

        self.fh = open(self.pathname, 'rb')

        magic = self.fh.read(8)
        if magic != self._expected_magic:
            raise TypeError('File is not a proper .png file.')

        return self

    def __exit__(self, type, val, tb):
        self.fh.close()

    def __iter__(self):
        return self

    def __next__(self):
        # Read the file in "Chunks"
        # See https://en.wikipedia.org/wiki/Portable_Network_Graphics#%22Chunks%22_within_the_file
        initial_data = self.fh.read(4)

        if self.fh is None or initial_data == b'':
           raise StopIteration
        else:
            # PNG chunk layout: len, type, data, crc
            chunk_len  = int.from_bytes(initial_data, byteorder='big')
            chunk_type = self.fh.read(4)
            chunk_data = self.fh.read(chunk_len)
            chunk_crc  = self.fh.read(4)
            return chunk_len, chunk_type, chunk_data, chunk_crc


# with PngReader('/Users/mvferr/Desktop/Screen Shot 2019-03-14 at 10.04.42.png') as reader:
#     for len, tp, data, crc in reader:
#         print(f"{len:06}, {tp}, {crc}")
