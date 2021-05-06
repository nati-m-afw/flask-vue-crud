<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr />
        <br /><br />
        
        <alert :msg="msg" v-if="showMsg"/>
        
        <button
          type="button"
          class="btn btn-success btn-sm"
          v-b-modal.book-modal
        >
          Add Book
        </button>
        <br /><br />

        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">
                    Update
                  </button>
                  <button type="button" class="btn btn-danger btn-sm">
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <b-modal
      ref="addBookModal"
      id="book-modal"
      title="Add a new book"
      hide-footer
    >
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group
          id="form-title-group"
          label="Title:"
          label-for="form-title-input"
        >
          <b-form-input
            id="form-title-input"
            type="text"
            v-model="addBookForm.title"
            required
            placeholder="Enter title"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group
          id="form-author-group"
          label="Author:"
          label-for="form-author-input"
        >
          <b-form-input
            id="form-author-input"
            type="text"
            v-model="addBookForm.author"
            required
            placeholder="Enter author"
          >
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
// better than fetch
import axios from "axios";
import Alert from '../components/Alert.vue';

export default {
  components: { Alert },
  data() {
    return {
      books: [],

      addBookForm: {
        title: "",
        author: "",
        read: [],
      },

      msg: '',
      showMsg: false,
    };
  },

  created() {
    this.getBooks();
  },

  componets: {
    alert: Alert,
  },

  methods: {
    getBooks() {
      fetch("http://localhost:5000/books")
        .then((response) => response.json())
        .then((response) => (this.books = response.books))
        .catch((err) => console.error(err));
    },

    addBook(payload) {
      axios
        .post("http://localhost:5000/books", payload)
        .then(() => {
          this.getBooks();
          this.msg = "Book Added!";
          this.showMsg = true;
        })
        .catch((err) => {
          console.error(err);
          this.getBooks();
        });
    },

    initForm() {
      this.addBookForm.title = "";
      this.addBookForm.author = "";
      this.addBookForm.read = [];
    },

    onSubmit(e) {
      e.preventDefault();
      this.$refs.addBookModal.hide();
      let read = this.addBookForm.read[0] ? true : false;
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        read,
      };
      this.addBook(payload);
      this.initForm();
    },

    onReset(e) {
      e.preventDefault();
      this.initForm();
    },
  },
};
</script>
