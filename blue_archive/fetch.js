  // 獲取content_cen元素
  let content = document.querySelector(".content_cen");
  // 獲取content_cen元素下的所有<p>元素
  let paragraphs = content.querySelectorAll("p");
  // 創建一個空數組，用於存儲符合條件的<p>元素
  let result = [];
  // 計數器，用於計算<hr>標籤的數量
  let hrCount = 0;
  // 遍歷所有<p>元素
  for (let p of paragraphs) {
    // 如果<p>元素的上一個兄弟元素是<hr>，則計數器加1
    if (p.previousElementSibling && p.previousElementSibling.tagName === "HR") {
      hrCount++;
    }
    // 如果計數器大於等於2，則跳出循環
    if (hrCount >= 2) {
      break;
    }
    // 如果<p>元素包含<strong>標籤，則在其內容前後各加一個底線字符'_'
    let strongs = p.querySelectorAll("strong");
    for (let strong of strongs) {
      strong.innerHTML = "_" + strong.innerHTML + "_";
      // 如果<strong>元素內部包含<span>標籤且<span>標籤帶有顏色，則在其內容前後各加一個'$'字符，並在後面標註顏色編碼
      let spans = strong.querySelectorAll("span");
      for (let span of spans) {
        if (span.style.color) {
          span.innerHTML =
            "$(" +
            span.style.color +
            ")" +
            span.innerHTML +
            "$";
        }
      }
    }
    // 如果<p>元素包含<img>標籤，則將其內容改為圖像的網址(src)
    if (p.querySelector("img")) {
      p.textContent = p.querySelector("img").src;
    }
    // 將<p>元素添加到結果數組中
    result.push(p);
  }
  // 返回結果數組
  return result;