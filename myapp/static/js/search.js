const resultBox = document.querySelector(".result-box");
const inputBox = document.getElementById("search-item");

inputBox.onkeyup = function () {
  let input = inputBox.value.trim(); // To remove leading/trailing whitespace

  if (input.length) {
    fetch(`/search/?search=${input}`)
      .then((response) => response.json())
      .then((books) => {
        console.log("Fetched books:", books); 
        resultBox.innerHTML = "";

        if (books.length > 0) {
          let resultList = "";
          for (const book of books) {
            resultList += `
              <a href="${book.page}" target="_blank" class="book"> 
                <img src="${book.image}" alt="${book.name}">
                <div class="b-details">
                  <h2>${book.name}</h2>
                  <p>Author: ${book.author}</p>
                  <p>Category: ${book.category}</p>
                </div>
              </a>`;
          }
          resultBox.innerHTML = resultList;
        } else {
          resultBox.innerHTML = "<p>No results found.</p>";
        }
      })
      .catch((error) => console.error("Error fetching books:", error));
  }
};

