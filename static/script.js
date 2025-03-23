let accessToken = null;

window.onload = () => {
  console.log("✅ Page loaded");
  fetchBooks(); // Show books for everyone (guest or admin)
};

// ✅ Admin Login
document.getElementById("login-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const email = document.getElementById("email").value;
  const password = document.getElementById("password").value;

  try {
    const res = await fetch("http://localhost:8000/api/admin/login/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const data = await res.json();
    if (res.ok) {
      accessToken = data.access;
      alert("Login successful!");

      document.getElementById("book-form").style.display = "block";
      document.getElementById("logout-btn").style.display = "block";
      document.getElementById("login-section").style.display = "none";

      fetchBooks(); // Refresh books with admin actions
    } else {
      alert("Login failed: " + (data.detail || "Invalid credentials"));
    }
  } catch (error) {
    console.error("Login error:", error);
    alert("Error logging in");
  }
});

// ✅ Admin Logout
document.getElementById("logout-btn").addEventListener("click", () => {
  accessToken = null;
  document.getElementById("book-form").style.display = "none";
  document.getElementById("logout-btn").style.display = "none";
  document.getElementById("login-section").style.display = "block";
  fetchBooks(); // Re-render books without admin tools
});

// ✅ Add Book
document.getElementById("add-book-form").addEventListener("submit", async (e) => {
  e.preventDefault();

  const book = {
    title: document.getElementById("title").value,
    author: document.getElementById("author").value,
    isbn: document.getElementById("isbn").value,
    publication_date: document.getElementById("publication_date").value,
  };

  try {
    const res = await fetch("http://localhost:8000/api/books/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: "Bearer " + accessToken,
      },
      body: JSON.stringify(book),
    });

    if (res.ok) {
      alert("Book added successfully!");
      document.getElementById("add-book-form").reset();
      fetchBooks();
    } else {
      const data = await res.json();
      alert("Error adding book: " + JSON.stringify(data));
    }
  } catch (error) {
    console.error("Add book error:", error);
  }
});

// ✅ Fetch & Display Books
async function fetchBooks() {
  try {
    const res = await fetch("http://localhost:8000/api/books/", {
      headers: accessToken
        ? { Authorization: "Bearer " + accessToken }
        : {},
    });

    const books = await res.json();
    const list = document.getElementById("book-list");
    list.innerHTML = "";

    if (!books.length) {
      list.innerHTML = "<p>No books found.</p>";
      return;
    }

    books.forEach((book) => {
      const div = document.createElement("div");
      div.className = "book-entry";
      div.innerHTML = `
        <b>${book.title}</b> by ${book.author} <br>
        ISBN: ${book.isbn} <br>
        Published: ${book.publication_date}
        ${accessToken ? `
          <br>
          <button class="action" onclick="editBook(${book.id}, '${book.title}', '${book.author}', '${book.isbn}', '${book.publication_date}')">✏️ Edit</button>
          <button class="action" onclick="deleteBook(${book.id})">🗑️ Delete</button>
        ` : ""}
      `;
      list.appendChild(div);
    });
  } catch (error) {
    console.error("Fetch error:", error);
    document.getElementById("book-list").innerHTML = "<p>Error loading books.</p>";
  }
}

// ✅ Edit Book
function editBook(id, title, author, isbn, pubDate) {
  const newTitle = prompt("Edit title", title);
  const newAuthor = prompt("Edit author", author);
  const newISBN = prompt("Edit ISBN", isbn);
  const newDate = prompt("Edit date", pubDate);

  fetch(`http://localhost:8000/api/books/${id}/`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + accessToken,
    },
    body: JSON.stringify({
      title: newTitle,
      author: newAuthor,
      isbn: newISBN,
      publication_date: newDate,
    }),
  })
    .then((res) => res.json())
    .then((data) => {
      alert("Book updated!");
      fetchBooks();
    });
}

// ✅ Delete Book
function deleteBook(id) {
  if (!confirm("Are you sure you want to delete this book?")) return;

  fetch(`http://localhost:8000/api/books/${id}/`, {
    method: "DELETE",
    headers: {
      Authorization: "Bearer " + accessToken,
    },
  }).then((res) => {
    if (res.ok) {
      alert("Book deleted");
      fetchBooks();
    } else {
      alert("Failed to delete book");
    }
  });
}
