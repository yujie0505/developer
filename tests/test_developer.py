from developer import __version__, config


def test_version():
    assert __version__ == "0.1.0"


def test_config():
    get_env = config.load(".env.test")

    assert get_env("OPENAI_API_KEY") == "openai-api-key"
