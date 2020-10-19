# uncommon

Uncommon is a Python package to generate uncommon phrases that can be used for passphrases or other use cases

## Getting Started

To use `uncommon` you can clone this repository or install from `pypi`.

### Installing

You can install `uncommon` using `pip`.

```
pip3 install uncommon
```

You can clone this repository and install the package directly using the following

```
git clone https://github.com/MSAdministrator/uncommon.git
cd uncommon
python3 setup.py install
```

## Using

Once you have `uncommon` installed, you can use it by importing the package and utilizing the built-in methods:

```python
from uncommon import Uncommon

print(Uncommon().get())
```

You can provide additional parameters like the desired separator and the number of words to include in your phrase:

```python
from uncommon import Uncommon

print(Uncommon(separator=';', count=10).get())
```

## Built With

* [carcass](https://github.com/MSAdministrator/carcass) - Python packaging template

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. 

## Authors

* Josh Rickard - *Initial work* - [MSAdministrator](https://github.com/MSAdministrator)

See also the list of [contributors](https://github.com/MSAdministrator/uncommon/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details
