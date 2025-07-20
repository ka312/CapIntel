# Executive Summary

The 2018-2019 season of the National Basketball Association (NBA) is about to start. It will be the 73rd season of the league and the 72nd season since the NBA adopted its current name.

The regular season begins on October 16, 2018, and ends on April 9, 2019. The playoffs will begin on April 13, 2019, and end with the NBA Finals in June 2019.

The defending champions are the Golden State Warriors, who won their third championship in four years by defeating the Cleveland Cavaliers in the 2018 NBA Finals. The Warriors will be looking to repeat as champions this season, but they will face stiff competition from teams like the Boston Celtics, Houston Rockets, and Philadelphia 76ers.

The NBA has made several changes to its rules for the upcoming season. One of the most significant changes is the elimination of the "one-and-done" rule, which required players to be at least one year removed from high school before they could enter the NBA draft. This rule change will allow players to enter the draft after just one season in college, giving them more time to develop their skills and potentially increasing the talent level in the league.

Another significant rule change is the implementation of a new shot clock, which will be reduced from 24 seconds to 23 seconds for non-free throw attempts. This change is intended to increase the pace of play and reduce the number of stalled possessions.

The NBA has also made changes to its All-Star Game format. For the first time since 1988, the game will not feature teams from the Eastern Conference and Western Conference. Instead, the top vote-getters from each conference will be drafted by captains LeBron James and Stephen Curry, who will serve as team captains for the game.

The NBA has also announced several new initiatives aimed at promoting social justice and addressing issues of racial inequality in America. These include a partnership with the National Association for the Advancement of Colored People (NAACP) to combat voter suppression, and a commitment to donate $30 million over three years to organizations working to address systemic racism and promote social justice.

Overall, the 2018-2019 NBA season promises to be an exciting one, with new rules, new faces, and renewed rivalries on display. Fans can look forward to watching some of the best basketball players in the world compete for championship glory.

# Industry Analysis

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7vlp1yeeACpl2T73VWUs6q8waV9im2VEmFpUJ6k5VzvKryb" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSGFpoBjuUq4m1kJtMl+zKr8jbTSmWkmFda9e6vvvQF1GMbUdAdi" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoJtKh7zXkeufYfR6jqamLVz6l5WRbTXU+q7qDhPjmawMDmPm" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q43O6s67veW9oiqPuMNntWlzEn27kCekZXNEFmXsqRTck9Tr+QyT1c" crossorigin="anonymous"></script>
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
            <label for="email">Correo:</label>
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

# Investment Thesis

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0ONyNtNWMOkwbHlZMidlL9vqOBn3n9A6VXanubHNJbS3QDPuno1DSPysjC" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VvesbMp5ua9eCU9SHmfKshsDrewGkez" crossorigin="anonymous"></script>
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

# Company Profiles

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
            width: 80%;
            margin: auto;
        }
        .form-group{
            margin-bottom: 15px;
        }
        .btn-primary{
            background-color: #3c8dbc !important;
            border-color: #3c8dbc !important;
        }
    </style>
</head>
<body>
<div class="container">
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="image">
        <button type="submit" name="upload">Upload</button>
    </form>
</div>
<?php
if(isset($_POST['upload'])){
    $target_dir = "uploads/";
    $target_file = $target_dir . basename($_FILES["image"]["name"]);
    move_uploaded_file($_FILES["image"]["tmp_name"], $target_file);
}
?>
</body>
</html>

# Due Diligence Analysis

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7ql5mVUYtju9C2/AjvPRA2ce762ynChpdRN3wIAxQnAvHucGZ" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSGFpoBjuUq4m1kJtMl9RzexethUWgc1ZJcMUyMaXQVEYrcGg7" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js" integrity="sha384-eMNCOe7tC1doHpGoJtKh6zY7Xl65+bLHq5c8NK4aKKr8txpY0GlbCTeZjcC7l2" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js" integrity="sha384-w1Q43O6s67unzVJLq0RkfjOrjDERJum9Jum4vsR061NZB4ggfnrU0eIRp62oi" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Formulario de registro</h1>
        <form action="{{route('register')}}" method="POST">
            @csrf
            <label for="name">Nombre:</label>
            <input type="text" name="name" id="name" placeholder="Ingrese su nombre" value="{{old('name')}}">
            @error('name')
                <small class="text-danger">{{$message}}</small>
            @enderror
            <br>
            <label for="email">Email:</label>
            <input type="email" name="email" id="email" placeholder="Ingrese su email" value="{{old('email')}}">
            @error('email')
                <small class="text-danger">{{$message}}</small>
            @enderror
            <br>
            <label for="password">Contraseña:</label>
            <input type="password" name="password" id="password" placeholder="Ingrese su contraseña">
            @error('password')
                <small class="text-danger">{{$message}}</small>
            @enderror
            <br>
            <label for="password_confirmation">Confirmar Contraseña:</label>
            <input type="password" name="password_confirmation" id="password_confirmation" placeholder="Confirme su contraseña">
            @error('password_confirmation')
                <small class="text-danger">{{$message}}</small>
            @enderror
            <br>
            <button type="submit" class="btn btn-primary">Registrarse</button>
        </form>
    </div>
</body>
</html>

# Investment Recommendations

<template>
    <div class="container">
      <h1>{{ title }}</h1>
      <p>{{ text }}</p>
      <button @click="changeTitle">Change Title</button>
    </div>
  </template>

  <script>
  export default {
    data() {
      return {
        title: 'Hello World',
        text: 'This is a simple Vue.js component.'
      };
    },
    methods: {
      changeTitle() {
        this.title = 'New Title';
      }
    }
  };
  </script>

  <style scoped>
  .container {
    border: 1px solid #ccc;
    padding: 20px;
    margin-bottom: 20px;
  }
  </style>

# Risk Factors and Mitigation

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/hrW7rl3fpDMTB0ip31pGvk8hRZg9SrrMareJ8Lx2ifJH6OhExus" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSGFpoBjuUq4m1kJtGZXgeDb7xwazRMNkMKZXge0pJYuAJ8A96Fr" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz4fnFO9gybBud7RUk2eFtKp+WJ0w7yYfoR2DZMP+PL/U1MSxX1GVYgTc" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js" integrity="sha384-cn7l7gDp0eyniUwwAZgrzDq6kC3l9L2xqqvVxIqJ7Red87W2aOBl9ClhhE9Fx9J" crossorigin="anonymous"></script>
</head>
<body>
    <div class="container">
        <h1>Formulario de registro</h1>
        <form action="{{ route('register') }}" method="POST">
            @csrf
            <div class="form-group">
                <label for="name">Nombre:</label>
                <input type="text" name="name" id="name" class="form-control" value="{{ old('name') }}" required>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" name="email" id="email" class="form-control" value="{{ old('email') }}" required>
            </div>
            <div class="form-group">
                <label for="password">Contraseña:</label>
                <input type="password" name="password" id="password" class="form-control" required>
            </div>
            <button type="submit" class="btn btn-primary">Registrarse</button>
        </form>
    </div>
</body>
</html>

# Appendices

The 2018-2019 school year is off to a great start! We are excited to welcome our new students and families, as well as those returning.

   Our first day of school was August 27th. Students were welcomed with a special assembly where they learned about the school's expectations for behavior and academics. They also had an opportunity to meet their teachers and classmates.

   Since then, students have been busy learning new things and making new friends. Our teachers are working hard to create engaging lessons that will help students succeed. We are also focusing on building a positive school culture where everyone feels valued and respected.

   We are looking forward to a great year! If you have any questions or concerns, please don't hesitate to contact us. We are here to help!