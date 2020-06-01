"""
This setup.py allows your python package to be installed. 
Please completely update the parameters in the opts dictionary. 
For more information, see https://stackoverflow.com/questions/1471994/what-is-setup-py
"""
import os
from setuptools import setup, find_packages

PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_env_variable(var_name, default=False):
    """
    Get the environment variable or return exception
    :param var_name: Environment Variable to lookup
    """
    try:
        return os.environ[var_name]
    except KeyError:
        from io import StringIO
        import configparser
        env_file = os.environ.get('PROJECT_ENV_FILE', PROJECT_ROOT_DIR + "/.env")
        try:
            config = StringIO()
            config.write("[DATA]\n")
            config.write(open(env_file).read())
            config.seek(0, os.SEEK_SET)
            cp = configparser.ConfigParser()
            cp.read_file(config)
            value = dict(cp.items('DATA'))[var_name.lower()]
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]
            os.environ.setdefault(var_name, value)
            return value
        except (KeyError, IOError):
            if default is not False:
                return default

            error_msg = "Either set the env variable '{var}' or place it in your " \
                        "{env_file} file as '{var} = VALUE'"
            raise EnvironmentError(error_msg.format(var=var_name, env_file=env_file))


PACKAGES = find_packages()

opts = dict(name='ProjectName',
            maintainer='Name1, Name2, etc',
            maintainer_email='your_email',
            description='Add short description',
            long_description=("""Add an even more detailed description"""),
            url='your_repo_url_here',
            license='MIT', # default license, change here and in the git repo if using a different license
            author='Name1, Name2, etc',
            author_email='your_email',
            version='0.1',
            packages= PACKAGES, #this corresponds to the directory-name of the python package you want installed
            test_packages= [], #this corresponds to the directory-name of any packages that are strictly for tests. will be conditionally installed.
            install_requires= ['os',
                              'pip',
                              'some_esoteric_package' 
                              'some_weird_private_package' #we can link this below and provide authorization to pull it
                             ],
            tests_require=['nose'], 
            test_suite='nose.collector',   
            dependency_links= ['https://somesitewithjusttherightpackagenotinpip.org/a/link/to/a/tarball#egg=some_esoteric_package',
                                'https://{}@github.com/FredHutch/MyWeirdSecretRepo/tarball/master#egg=some_weird_private_package'.format(get_env_variable('HDCGITAUTHTOKEN'))
                               ],
            
           )

setup(**opts)

