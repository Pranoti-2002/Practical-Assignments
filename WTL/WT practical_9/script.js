function CalculatorCtrl($scope) {
  
    $scope.a = 0;
    $scope.b = 0;
    $scope.operation = '+';
    
    $scope.na = function() {
      return $scope.a-0;
    }
    
    $scope.nb = function() {
      return $scope.b - 0;
    }
    
    $scope.inca = function() {
      $scope.a = $scope.na() + 1;
    }
    
    $scope.incb = function() {
      $scope.b = $scope.nb() + 1;
    }
    
    $scope.deca = function() {
      $scope.a = $scope.na() - 1;
    }
    
    $scope.decb = function() {
      $scope.b = $scope.nb() - 1;
    }
    
    $scope.calculate = function() {
      if($scope.operation == '+') {
        return $scope.na() + $scope.nb();
      }
      if($scope.operation == '-') {
        return $scope.a - $scope.b;
      }
      if($scope.operation == '*') {
        return $scope.a * $scope.b;
      }
      if($scope.operation == '/') {
        return $scope.a / $scope.b;
      }
      return "undef";
    }
  }
  