<template>
  <div id="app">
    <Header/>
    <Middle/>
    <Footer/>
  </div>
</template>

<script>
import axios from "axios";
import Footer from "@/components/Footer.vue";
import Header from "@/components/Header.vue";
import Middle from "@/components/Middle.vue";

export default {
  name: 'App',
  components: {
    Middle,
    Header,
    Footer,
  },
  data: function () {
    return {
      user: null,
      posts: [],
      cycles: [],
    }
  },
  beforeMount() {
    if (localStorage.getItem("jwt") && !this.user) {
      this.$root.$emit("onJwt", localStorage.getItem("jwt"));
    }

    axios.get("/api/1/posts").then(response => {
      this.posts = response.data;
    });

    // axios.get("/api/1/cycles").then(response => {
    //     this.cycles = response.data;
    // });
  },
  beforeCreate() {
    this.$root.$on("onUpdatePosts", () => {
      axios.get("/api/1/posts").then(response => {
        this.posts = response.data;
      });
    });

    this.$root.$on("onCorrect", (login, password) => {
      if (password === "") {
        this.$root.$emit("onEnterValidationError", "Password is required");
        return;
      }

      axios.post("/api/1/jwt", {
        login, password
      }).then(response => {
        localStorage.setItem("jwt", response.data);
        this.$root.$emit("onJwt", response.data);
      }).catch(error => {
        // alert(error.response.data);
        this.$root.$emit("onEnterValidationError", error.response.data);
      });
    });

    this.$root.$on("onRegister", (login, name, password, confirmPassword) => {
      axios.post("/api/1/users", {
        login, name, password, confirmPassword
      }).then(response => {
        localStorage.setItem("jwt", response.data);
        this.$root.$emit("onJwt", response.data);
        // this.$root.$emit("onUpdateUsers");
      }).catch(error => {
        this.$root.$emit("onRegisterValidationError", error.response.data);
      });
    });

    this.$root.$on("onJwt", (jwt) => {
      localStorage.setItem("jwt", jwt);

      axios.get("/api/1/users/auth", {
        params: {
          jwt
        }
      }).then(response => {
        this.user = response.data;
        this.$root.$emit("onChangePage", "IndexPage");
      }).catch(() => this.$root.$emit("onLogout"))
    });

    this.$root.$on("onLogout", () => {
      localStorage.removeItem("jwt");
      this.user = null;
    });

    this.$root.$on("onWritePost", (title, text) => {
      const jwt = localStorage.getItem("jwt");
      if (!jwt) {
        this.$root.$emit("onWritePostValidationError", "Log in before writing posts!");
        return;
      }
      axios.post(
          "/api/1/posts",
          {
            title, text,
          },
          {
            params: {jwt}
          }
      ).then(() => {
        this.$root.$emit("onChangePage", "IndexPage");
        this.$root.$emit("onUpdatePosts");
      }).catch(error => {
        this.$root.$emit("onWritePostValidationError", error.response.data);
      });
    });

    // this.$root.$on("onWriteComment", (postId, text) => {
    //     const jwt = localStorage.getItem("jwt");
    //     if (!jwt) {
    //         this.$root.$emit("onWriteCommentValidationError", "Log in before writing comments!");
    //         return;
    //     }
    //     let url = `/api/1/post/${postId}/comment`;
    //     axios.post(
    //         url,
    //         {
    //             text,
    //         },
    //         {
    //             params: {jwt}
    //         }
    //     ).then(response => {
    //         this.posts = response.data;
    //     }).catch(error => {
    //         this.$root.$emit("onWriteCommentValidationError", error.response.data);
    //     });
    // });
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
