import sys
sys.path.append("../../config")
import write_common_headers

P2C_NAME = 'stub'
P2C_STUB_MAJOR_VERSION = 0
P2C_STUB_MINOR_VERSION = 1
P2C_STUB_PATCH_VERSION = 0

stub_version = write_common_headers.write_version_header(P2C_NAME,
                                                         P2C_STUB_MAJOR_VERSION,
                                                         P2C_STUB_MINOR_VERSION,
                                                         P2C_STUB_PATCH_VERSION)
