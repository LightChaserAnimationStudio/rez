config_version = 0
name = 'foo'
version = '1.0.0'
authors = ["joe.bloggs"]
uuid = "8031b8a1b1994ea8af86376647fbe530"
description = "foo thing"

build_requires = ["nover"]

private_build_requires = ["build_util", "python"]

def commands():
    env.PYTHONPATH.append('{root}/python')
