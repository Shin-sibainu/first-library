import setuptools

setuptools.setup(
  name="hello-world",
  version="0.0",
  author="Shibainu",
  description="Say Hello.",
  packages=["hello_world"],
  package_dir={"hello_world": "src/hello_world"},
  python_requires=">=3.8"
)