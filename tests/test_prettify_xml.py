# -*- coding: utf-8 -*-
import os
import codecs

from click.testing import CliRunner
from bs4 import BeautifulSoup

from nlppln.commands.prettify_xml import prettify_xml


def test_prettify_xml():
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.makedirs('in')
        os.makedirs('out')
        with open('in/test.xml', 'w') as f:
            xml = '<?xml version="1.0" encoding="utf-8"?>\n<document>\n' \
                  '<word w_id="242" value="test" total_analysis="11">\n' \
                  '<analysis a_id="1" additional_info=""/>\n' \
                  '</word>\n</document>'
            f.write(xml)

        result = runner.invoke(prettify_xml, ['in/test.xml',
                                              '--out_dir', 'out'])

        assert result.exit_code == 0

        assert os.path.exists('out/test.xml')

        with codecs.open('out/test.xml', 'r', encoding='utf-8') as f:
            pretty = f.read()

        assert pretty == BeautifulSoup(xml, 'xml').prettify()
