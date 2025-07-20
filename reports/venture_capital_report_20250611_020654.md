# Executive Summary

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Skd1v" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-wAxZ6bc9sku7TLVnlNIMmoMeyXynoY0w0IDaB4FzdbOEaW9W9781Dsw6JFqV6sD" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h2>Formulario de registro</h2>
        <form action="{{route('register')}}" method="POST">
            @csrf
            <div class="form-group">
                <label for="name">Nombre:</label>
                <input type="text" name="name" id="name" class="form-control" placeholder="Ingrese su nombre">
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" name="email" id="email" class="form-control" placeholder="Ingrese su email">
            </div>
            <div class="form-group">
                <label for="password">Contraseña:</label>
                <input type="password" name="password" id="password" class="form-control" placeholder="Ingrese su contraseña">
            </div>
            <button type="submit" class="btn btn-primary">Registrarse</button>
        </form>
    </div>
</body>
</html>

# Industry Analysis

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <script src="js/jquery-3.2.1.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <style type="text/css">
        .container{
            margin: 0 auto;
            width: 80%;
        }
        .header{
            background-color: #f1c40f;
            padding: 20px;
            text-align: center;
            color: white;
        }
        .footer{
            background-color: #f1c40f;
            padding: 20px;
            text-align: center;
            color: white;
        }
    </style>
</head>
<body>
<div class="container">
    <header class="header">
        <h1>Welcome to my website</h1>
    </header>
    <main>
        <article>
            <h2>About me</h2>
            <p>I am a student of Computer Science and Engineering at the University of Dhaka. I love programming and web development.</p>
        </article>
        <article>
            <h2>My Skills</h2>
            <ul>
                <li>HTML</li>
                <li>CSS</li>
                <li>JavaScript</li>
                <li>PHP</li>
                <li>MySQL</li>
                <li>Bootstrap</li>
            </ul>
        </article>
    </main>
    <footer class="footer">
        <p>&copy; 2017 All rights reserved.</p>
    </footer>
</div>
</body>
</html>

# Investment Thesis

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <style type="text/css">
        .container{
            margin-top: 100px;
        }
    </style>
</head>
<body>
<div class="container">
    <h2>Login</h2>
    <form action="login.php" method="post">
        <input type="text" name="username" placeholder="Username" required>
        <br><br>
        <input type="password" name="password" placeholder="Password" required>
        <br><br>
        <button type="submit" class="btn btn-primary">Login</button>
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
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7rl3fpDMTB0IPSSvQGVcx61CRVicqCU+b9a9l7I7/AMdtgjqx" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSS95gLbOKn0bJ2RbWCl+0oGXatLs04OUHppBqz4mG6Mega75kxw" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoJtKh6zY7Xl6zA0LfJUr9z78ELkJV3kewxql1rFgeP88tB05JS7" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q43O6s67veW9oiqPuMNnt2e2IiA68v+yKJIDaNzpZ3ZC77Vd9pbilVyd6i" crossorigin="anonymous"></script>
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
                <label for="email">Correo:</label>
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
            <button type="submit" class="btn btn-primary">Registrarse</button>
        </form>
    </div>
</body>
</html>

# Due Diligence Analysis

[![Build Status](https://travis-ci.org/jamesd1984/sbt-react.svg?branch=master)](https://travis-ci.org/jamesd1984/sbt-react)

# sbt-react

A Scala build tool plugin for [React](http://facebook.github.io/react/) and [Webpack](https://webpack.github.io/).

## Features

* Automatic compilation of React components on file change
* Hot module replacement (HMR) for faster development
* Production builds with minification, source maps and tree shaking
* Integration with [sbt-web](https://github.com/jamesd1984/sbt-web) for serving your app locally
* Support for [React Native](https://facebook.github.io/react-native/) projects

## Requirements

* Scala 2.11 or 2.12
* SBT 0.13.8 or later
* Node.js 4.x or later (for Webpack)

## Installation

Add the following line to your `project/plugins.sbt` file:

```scala
addSbtPlugin("com.jamesd1984" % "sbt-react" % "0.3.2")
```

Then run `sbt update` to download the plugin and its dependencies.

## Usage

### React projects

To create a new project, use the following command:

```sh
$ sbt new com.jamesd1984/sbt-react-seed.g8
```

This will generate a new Scala project with a basic React setup.

### React Native projects

To create a new React Native project, use the following command:

```sh
$ sbt new com.jamesd1984/sbt-react-native-seed.g8
```

This will generate a new Scala project with a basic React Native setup.

### Configuration

The plugin uses the `webpackConfig` setting to determine how to configure Webpack for your project. You can define this setting in your build definition like so:

```scala
lazy val root = Project(idName, file(".")).settings(
  webpackConfig := Some(new ReactWebpackConfig)
)
```

The `ReactWebpackConfig` class is a simple wrapper around the [default Webpack configuration for React](https://github.com/reactjs/redux/blob/master/webpack.config.js). You can customise this configuration by extending the `ReactWebpackConfig` class and overriding its methods.

### Development

To start a development server, run:

```sh
$ sbt react/start
```

This will compile your React components on file change and serve them at `http://localhost:8080`. You can open this URL in your browser to view your app.

### Production

To build a production version of your app, run:

```sh
$ sbt react/package
```

This will create an optimised bundle at `target/scala-2.11/main/webapp/static/js/bundle.min.js`. You can include this file in your HTML to serve your app.

## License

sbt-react is released under the [MIT license](LICENSE).

# Investment Recommendations

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7vlp1yeeACpl2T73VWUs6q8waV9im2VEmFpUJ6k5VzvKryb" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSGFpoBjuUq4m1kJtGZXgeSeYmTdgV79w6zynNqfxz/oWvScq2O" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz4fnFO9gybBud7RUk2eFtKp+WJ0gYt7zc5NlqJ9G3h8v8u1Up1ASXjD" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q43O6s67un5kVy0Vp5jGFJck7X6Af50e36aY7qdbGl06pt4xqD8d8EAz9GKh4" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <form action="{{route('register')}}" method="post">
            @csrf
            <label for="name">Name:</label>
            <input type="text" name="name" id="name" value="{{old('name')}}">
            @error('name')
                <p class="text-danger">{{$message}}</p>
            @enderror
            <br>
            <label for="email">Email:</label>
            <input type="text" name="email" id="email" value="{{old('email')}}">
            @error('email')
                <p class="text-danger">{{$message}}</p>
            @enderror
            <br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password">
            @error('password')
                <p class="text-danger">{{$message}}</p>
            @enderror
            <br>
            <button type="submit">Register</button>
        </form>
    </div>
</body>
</html>

# Risk Factors and Mitigation

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7vlp1yeeACtndhLo/i/PfjWuHr8l6+tByD97e5qfsTh/drLv" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSGFpoBjuUq4m1kJtGZPz5pqIl+eqMem17CwUR90eCBnJLUnhoe" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoJtKh6zY7Xs5k8ygoPsfty+o/shoj+xqOGOzDWlzcvh80r8" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q43O6s67unzVJLq0RkfjOrjDERJumTRbUeeUJ6Wfi2Onsl4FXe506T13zKaU7Rs" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Formulario de registro</h1>
        <form action="{{route('register')}}" method="POST">
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

# Appendices

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <script src="js/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <style type="text/css">
        .container{
            width: 100%;
            height: 50px;
            background-color: #f2f2f2;
        }
        .navbar-brand{
            font-size: 30px;
            color: #fff;
        }
    </style>
</head>
<body>
<div class="container">
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="#">LOGO</a>
            </div>
            <ul class="nav navbar-nav">
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </div>
    </nav>
</div>
</body>
</html>