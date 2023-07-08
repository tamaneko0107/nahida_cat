let result = []
var colors = document.querySelectorAll(".content_cen span[style*='color'], .content_cen strong[style*='color']");

for (let color of colors) {
  let colorCode = color.style.color;
  result.push(colorCode);
}
return result;