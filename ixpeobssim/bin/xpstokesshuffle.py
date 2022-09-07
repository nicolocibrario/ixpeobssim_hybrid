#!/usr/bin/env python
#
# Copyright (C) 2022, the ixpeobssim team.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

"""xpstokesshuffle app.
"""

from __future__ import print_function, division

import numpy

from ixpeobssim.evt.event import xEventFile
from ixpeobssim.utils.argparse_ import xArgumentParser
from ixpeobssim.utils.logging_ import logger
from ixpeobssim.utils.misc import process_file_list
from ixpeobssim.utils.os_ import check_output_file

#pylint: disable=no-member, invalid-name

__description__ = \
"""Process a level-2 file and shuffle the value of the Q and U columns across the
events.
"""

PARSER = xArgumentParser(description=__description__)
PARSER.add_filelist()
PARSER.add_seed(default=1)
PARSER.add_suffix('stokesshuffle')
PARSER.add_overwrite()


def _process_file(file_path, **kwargs):
    """Process a single file.
    """
    suffix = '%s%04d' % (kwargs.get('suffix'), kwargs.get('seed'))
    output_file_path = check_output_file(file_path, suffix, kwargs.get('overwrite'))
    if output_file_path is None:
        return None
    event_file = xEventFile(file_path)
    perm = numpy.random.default_rng().permutation(event_file.num_events())
    q = event_file.q_data()[perm]
    u = event_file.u_data()[perm]
    event_file.set_column('EVENTS', 'Q', q)
    event_file.set_column('EVENTS', 'U', u)
    event_file.write(output_file_path, overwrite=kwargs.get('overwrite'))
    return output_file_path


def xpstokesshuffle(**kwargs):
    """Application entry point.
    """
    seed = kwargs.get('seed')
    logger.info('Setting the random seed to %d...', seed)
    numpy.random.seed(seed)
    return process_file_list(_process_file, kwargs.get('filelist'), **kwargs)


def main():
    """main() entry point.
    """
    xpstokesshuffle(**PARSER.parse_args().__dict__)



if __name__ == '__main__':
    main()
