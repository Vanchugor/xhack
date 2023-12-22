<template>

  <div class="container">
    <div>
      <h2>Коррекция изображения</h2>
      <hr/>
      <div class="chooser">
        <label>Files
          <input type="file" multiple @change="handleFileUploads( $event )"/>
        </label>
      </div>
      <button v-on:click="submitFiles()">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CorrectionPage",
  data() {
    return {
      files: ''
    }
  },
  methods: {
    handleFileUpload(event) {
      this.files = event.target.files;
    },
    submitFiles() {
      let formData = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];
        formData.append('files[' + i + ']', file);
      }

      // axios.postForm('/api/correct', {
      //   my_field: 'my value',
      //   my_buffer: new Blob([1, 2, 3]),
      //   my_file: this.files // FileList will be unwrapped as sepate fields
      // }).then(function () {
      //   console.log('SUCCESS!!');
      // })
      //     .catch(function () {
      //       console.log('FAILURE!!');
      //     });

      axios.post('/api/correct',
          {
            file: this.files[0]
          },
          {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
          }
      ).then(function () {
        console.log('SUCCESS!!');
      })
          .catch(function () {
            console.log('FAILURE!!');
          });
    }
  }
}
</script>

<style scoped>
.chooser {
  margin-bottom: 0.5rem;
}

.variant {
  margin-bottom: 0.5rem;
}

label {
  margin-right: 0.5rem;
}
</style>