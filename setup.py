import setuptools

setuptools.setup(name='rl_tools',
      version='0.1',
      description='Custom rl tools',
      #url='http://github.com/storborg/funniest',
      author='Philippe Proctor',
      package_dir={"": "rl_tools"},
      packages=["rl_tools"],#setuptools.find_packages(where="rl_tools"),
      python_requires=">=3.6",
      license='MIT',
      #packages=['rl_tools'],
      zip_safe=False)