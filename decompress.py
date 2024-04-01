import zlib

with open("data/22557847_detail.zio", "rb") as file:
    compressed_data = file.read()

decompressed_data = zlib.decompress(compressed_data)
json_string = decompressed_data.decode()

print(json_string)