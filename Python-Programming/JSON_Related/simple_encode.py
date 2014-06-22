#python3

# Basic implementations -- may be slow-ish
def array_to_json(arr):
	"""Dump an array to JSON, after converting it to a list."""
    return json.dumps(arr.tolist())

def json_to_array(string, dtype):
	"""Create an array from a JSON string, as the specified data type.""" 
    return np.fromiter(json.loads(string),dtype)

# Using Base64 encoding
def Base64Encode(ndarray):
	"""Encode with Base64 encoding."""
    return json.dumps([str(ndarray.dtype),base64.b64encode(ndarray),ndarray.shape])

def Base64Decode(jsonDump):
	"""Decode a Base64 JSON dump."""
    loaded = json.loads(jsonDump)
    dtype = np.dtype(loaded[0])
    arr = np.frombuffer(base64.decodestring(loaded[1]),dtype)
    if len(loaded) > 2:
        return arr.reshape(loaded[2])
    return arr
