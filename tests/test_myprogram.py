from unittest.mock import patch

from click.testing import CliRunner

from src.code import myprogram


def test_regular_function():
    with patch('src.code.myprogram.os.path.exists') as mocked_exists:
        mocked_exists.side_effect = [True, False]
        assert myprogram.regular_function() == ["Exist", "Does not exist"]


def test_regular_function_shutil():
    with patch('src.code.myprogram.shutil.get_archive_formats') as mocked_exists:
        mocked_exists.side_effect = [True, False]
        assert myprogram.regular_function_shutil() == ["First", "Second"]


def test_foo_os():
    runner = CliRunner()
    with patch('src.code.myprogram.os.path.exists') as mocked_exists:
        mocked_exists.side_effect = [True, False]
        result = runner.invoke(myprogram.command_foo_os)
        assert result.exit_code == 0
        assert all(i in result.output for i in ["Exist", "Does not exist"])


def test_foo_pathlib():
    runner = CliRunner()
    with patch('src.code.myprogram.Path.exists') as mocked_exists:
        mocked_exists.side_effect = [True, False]
        result = runner.invoke(myprogram.command_foo_pathlib)
        assert result.exit_code == 0
        assert all(i in result.output for i in ["Exist", "Does not exist"])