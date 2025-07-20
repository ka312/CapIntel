# Executive Summary

[![Build Status](https://travis-ci.org/joshuamcintyre/react-native-app.svg?branch=master)](https://travis-ci.org/joshuamcintyre/react-native-app)

# React Native App

A simple app using [React Native](http://facebook.github.io/react-native/) and [Redux](http://redux.js.org/).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* [Node.js](https://nodejs.org/) (v6.9.1 or later)
* [npm](https://www.npmjs.com/) (3.8.0 or later)
* [Xcode](https://developer.apple.com/xcode/) (7.3.1 or later) for iOS development
* [Android Studio](https://developer.android.com/studio/) for Android development

### Installing

Clone the repository and navigate to the project directory:
```
git clone https://github.com/joshuamcintyre/react-native-app.git
cd react-native-app
```

Install the dependencies:
```
npm install
```

Link the native libraries for iOS and Android:

#### iOS

* Open `ios/ReactNativeApp.xcworkspace` in Xcode
* Select the project in the left sidebar
* In the General tab, under Linked Frameworks and Libraries, make sure that `React` is checked
* In the Build Phases tab, under Target Dependencies, make sure that `React` is checked
* In the Build Settings tab, search for `Embedded Content Contains` and set it to `Yes`
* Run the project on an iOS simulator or a physical device

#### Android

* Open `android/app/build.gradle` in Android Studio
* Add the following line to the dependencies section:
```
implementation project(':react-native-cli')
```
* Sync the Gradle files
* Run the project on an Android emulator or a physical device

### Running the app

#### iOS

* Open `ios/ReactNativeApp.xcworkspace` in Xcode
* Select the scheme for the simulator you want to run on
* Press the Run button

#### Android

* Open `android/app/build.gradle` in Android Studio
* Set the `debug.packageName` property to your app's package name (e.g., `com.example.myapp`)
* Sync the Gradle files
* Press the Run button

## Built With

* [React Native](http://facebook.github.io/react-native/) - A framework for building native apps using only JavaScript and React
* [Redux](http://redux.js.org/) - A predictable state container for JavaScript apps

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/joshuamcintyre/react-native-app/tags).

## Authors

* **Joshua McIntyre** - *Initial work* - [JoshuaMcIntyre](https://github.com/joshuamcintyre)

See also the list of [contributors](https://github.com/joshuamcintyre/react-native-app/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

# Industry Analysis

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7rl3fpDMTB0ip31pGvwCCapZVf7P9WkbHTm8+FordvvA5V1MO" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <div class="container">
        <h2>Formulario de registro</h2>
        <form id="registro" action="registro.php" method="post">
            <label for="nombre">Nombre:</label>
            <input type="text" name="nombre" id="nombre" required>
            <br>
            <label for="apellido">Apellido:</label>
            <input type="text" name="apellido" id="apellido" required>
            <br>
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" required>
            <br>
            <label for="password">Contraseña:</label>
            <input type="password" name="password" id="password" required>
            <br>
            <button type="submit">Registrarse</button>
        </form>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz4fnFO9gybBud7Rde0Cc5eo8LXs7U5juuJJ0daEAqFxSxWC2rswrfCt9" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzDq6kC3l9L11dhAltnd7xbKbTf8tj7v7v8+9o3d128CA" crossorigin="anonymous"></script>
    <script src="registro.js"></script>
</body>
</html>

# Investment Thesis

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7rl3fpDMTB0ip31pGvwCCapZVf7P9WkbHTm8+F9IfY9F56y" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSGFpoBjuUq4m1kJtGZXgeDb7xIg9UOnYW6TonGeWMf9aCscSfOK" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz4fnFO9gybBud7Rde0Cx57hApidob1+UrRNWuFf1vd+zjhEs3aH4XKLg" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/js/bootstrap.min.js" integrity="sha384-kjU+l4N7tL4zKr0BTxMsXh+6aMvFBzF027St6qok7wJvAsI6o31YzOgA6dS7twk" crossorigin="anonymous"></script>
    <style>
        .container{
            margin-top: 5%;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>Formulario de registro</h1>
    <form action="{{route('register')}}" method="post">
        @csrf
        <label for="name">Nombre:</label>
        <input type="text" name="name" id="name" value="{{old('name')}}">
        @error('name')
            <small class="text-danger">{{$message}}</small>
        @enderror
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email" id="email" value="{{old('email')}}">
        @error('email')
            <small class="text-danger">{{$message}}</small>
        @enderror
        <br>
        <label for="password">Contraseña:</label>
        <input type="password" name="password" id="password">
        @error('password')
            <small class="text-danger">{{$message}}</small>
        @enderror
        <br>
        <button type="submit">Registrarse</button>
    </form>
</div>
</body>
</html>

# Company Profiles

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7rlH7YTMjEt1uS0+hOmdVVk0A9JnacnQvdF1v9hyowMpPX9" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoJtKh6zY4sFwFvtxTjAkkYXZgTT9w80KEhaGXL3ekNz4yl5MiH" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q43O6s67unzVJLq0RkfjOrjDERJumAAacHMOmrK9Tr29duI5Xwh9" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Formulario de registro</h1>
        <form action="{{route('register')}}" method="POST">
            @csrf
            <div class="form-group">
                <label for="name">Nombre:</label>
                <input type="text" name="name" id="name" class="form-control" value="{{old('name')}}">
                @error('name')
                    <small class="text-danger">{{$message}}</small>
                @enderror
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" name="email" id="email" class="form-control" value="{{old('email')}}">
                @error('email')
                    <small class="text-danger">{{$message}}</small>
                @enderror
            </div>
            <div class="form-group">
                <label for="password">Contraseña:</label>
                <input type="password" name="password" id="password" class="form-control" value="{{old('password')}}">
                @error('password')
                    <small class="text-danger">{{$message}}</small>
                @enderror
            </div>
            <div class="form-group">
                <label for="password_confirmation">Confirmar contraseña:</label>
                <input type="password" name="password_confirmation" id="password_confirmation" class="form-control" value="{{old('password_confirmation')}}">
            </div>
            <button type="submit" class="btn btn-primary">Registrarse</button>
        </form>
    </div>
</body>
</html>

# Due Diligence Analysis

[![Build Status](https://travis-ci.org/jamesd1984/python-ssh-keygen.svg?branch=master)](https://travis-ci.org/jamesd1984/python-ssh-keygen)

# python-ssh-keygen

A Python implementation of the SSH key generation process, using OpenSSL.

## Installation

```bash
pip install git+https://github.com/jamesd1984/python-ssh-keygen.git
```

## Usage

### Generate a new RSA key pair

```python
from ssh_keygen import generate_rsa_key

private_key, public_key = generate_rsa_key(bits=2048)
```

### Generate a new DSA key pair

```python
from ssh_keygen import generate_dsa_key

private_key, public_key = generate_dsa_key()
```

### Generate a new ECDSA key pair (NIST P-256)

```python
from ssh_keygen import generate_ecdsa_key

private_key, public_key = generate_ecdsa_key()
```

## License

This project is licensed under the MIT license. See [LICENSE](LICENSE) for more information.

# Investment Recommendations

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7rl3fpDMTB0ip31pGvk8hRZg9SrrMareJ8Lx2ifJH6OhExus" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoJtKh6zY7Xl65+bLASsUkpF+0OnzgR2NHtq+hp9lX/TQyx1A" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q43O6s67un5kVy0Vp5jGFJck7X6Af50e36aY77DdTGa63wasDI/NfBzc5v829K" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Formulario de registro</h1>
        <form action="{{route('register')}}" method="post">
            @csrf
            <label for="name">Nombre:</label>
            <input type="text" name="name" id="name" value="{{old('name')}}">
            @error('name')
                <small class="text-danger">{{$message}}</small>
            @enderror
            <br>
            <label for="email">Email:</label>
            <input type="text" name="email" id="email" value="{{old('email')}}">
            @error('email')
                <small class="text-danger">{{$message}}</small>
            @enderror
            <br>
            <label for="password">Contraseña:</label>
            <input type="password" name="password" id="password">
            @error('password')
                <small class="text-danger">{{$message}}</small>
            @enderror
            <br>
            <button type="submit">Registrarse</button>
        </form>
    </div>
</body>
</html>

# Risk Factors and Mitigation

<template>
    <div class="container">
      <h1>{{ title }}</h1>
      <p>{{ message }}</p>
      <button @click="handleClick">Click me</button>
    </div>
  </template>

  <script>
  export default {
    data() {
      return {
        title: 'Welcome to Vue.js!',
        message: 'This is a simple Vue.js application.',
      };
    },
    methods: {
      handleClick() {
        alert('Button clicked!');
      },
    },
  };
  </script>

  <style scoped>
  .container {
    text-align: center;
  }
  button {
    margin-top: 20px;
  }
  </style>

# Appendices

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7vlp1yeeACpl2T73VWUs6q8waV9im2VEmFpjDqH1wEJPglwwSl slink rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
        <h1>Formulaire de connexion</h1>
        <form action="connexion.php" method="post">
            <label for="email">Email : </label>
            <input type="text" name="email" id="email" required>
            <br>
            <label for="password">Mot de passe : </label>
            <input type="password" name="password" id="password" required>
            <br>
            <button type="submit">Connexion</button>
        </form>
    </div>
</body>
</html>