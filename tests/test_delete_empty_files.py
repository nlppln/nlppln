import os

from click.testing import CliRunner

from nlppln.commands.delete_empty_files import delete_empty_files


def test_delete_empty_files_different_in_and_out_directories():
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.makedirs('in')
        os.makedirs('out')
        with open('in/empty1.txt', 'w') as f:
            f.write('   \n\n ')
        with open('in/empty2.txt', 'w') as f:
            pass
        with open('in/not_empty.txt', 'w') as f:
            f.write('not empty\n')
        result = runner.invoke(delete_empty_files, ['in', '--out_dir', 'out'])

        assert result.exit_code == 0

        assert not os.path.exists('out/empty1.txt')
        assert not os.path.exists('out/empty2.txt')

        assert os.path.exists('out/not_empty.txt')


def test_delete_empty_files_equal_in_and_out_directories():
    runner = CliRunner()
    with runner.isolated_filesystem():
        os.makedirs('in')
        with open('in/empty1.txt', 'w') as f:
            f.write('   \n\n ')
        with open('in/empty2.txt', 'w') as f:
            pass
        with open('in/not_empty.txt', 'w') as f:
            f.write('not empty\n')
        result = runner.invoke(delete_empty_files, ['in', '--out_dir', 'in'])

        assert result.exit_code == 0

        assert not os.path.exists('in/empty1.txt')
        assert not os.path.exists('in/empty2.txt')

        assert os.path.exists('in/not_empty.txt')
