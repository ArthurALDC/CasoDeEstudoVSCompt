function palindrome(str) {
  // Remove espaços em branco e caracteres especiais, e converte para letras minúsculas
  str = str.toLowerCase().replace(/[^a-z0-9]/g, '');

  var length = str.length;
  for (var i = 0, j = length - 1; i < j; i++, j--) {
    if (str[i] !== str[j]) {
      return false;
    }
  }

  return true;
}

console.log(palindrome("race car")); // true
