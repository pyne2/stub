import sys
sys.path.append("../../config")
import write_common_headers

P2_NAME = '_'.join(__file__.split('_')[1:-1])
MAJOR_VERSION = 0
MINOR_VERSION = 1
PATCH_VERSION = 0

stub_version = write_common_headers.write_version_header(P2_NAME,
                                                         MAJOR_VERSION,
                                                         MINOR_VERSION,
                                                         PATCH_VERSION)
