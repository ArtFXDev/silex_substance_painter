# pylint: skip-file
name = "silex_substance_painter"
version = "0.1.0"

authors = ["ArtFx TD gang"]

description = """
    Set of python module and Substance Painter config to integrate Painter in the silex pipeline
    Part of the Silex ecosystem
    """

vcs = "git"

build_command = "python {root}/script/build.py {install}"


def commands():
    """
    Set the environment variables for silex_substance_painter
    """
    env.SILEX_ACTION_CONFIG.prepend("{root}/silex_substance_painter/config")
    env.PYTHONPATH.append("{root}")
    env.SBS_DESIGNER_PYTHON_PATH.append("{root}/startup")


@late()
def requires():
    major = str(this.version.major)
    silex_requirement = ["silex_client"]
    if major in ["dev", "beta", "prod"]:
        silex_requirement = [f"silex_client-{major}"]

    return ["substance_painter", "python-3.7"] + silex_requirement
