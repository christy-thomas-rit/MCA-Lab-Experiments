<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $number = isset($_POST["number"]) ? $_POST["number"] : "";

    if (!is_numeric($number)) {
        echo "Invalid input. Please enter a valid number.";
        exit;
    }

    $number = (int)$number;

    function factorial($n) {
        if ($n < 0) {
            return "Factorial is not defined for negative numbers.";
        } elseif ($n == 0 || $n == 1) {
            return 1;
        } else {
            return $n * factorial($n - 1);
        }
    }

    $result = factorial($number);
    echo "The factorial of $number is $result";
}

?>

