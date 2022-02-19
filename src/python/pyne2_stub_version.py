import sys
sys.path.append("../../config")
import write_common_headers

# Rename _STUB_ in this file to something unique to this module and
# replace/remove this commentß
P2_NAME = 'stub'
P2_STUB_MAJOR_VERSION = 0
P2_STUB_MINOR_VERSION = 1
P2_STUB_PATCH_VERSION = 0

stub_version = write_common_headers.write_version_header(P2_NAME,
                                                         P2_STUB_MAJOR_VERSION,
                                                         P2_STUB_MINOR_VERSION,
                                                         P2_STUB_PATCH_VERSION)
