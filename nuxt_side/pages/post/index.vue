
<template>
  <div class="container">
    <h1>
      Post List
    </h1>
    <v-row>
      <v-col cols="3">
        <v-text-field v-model="search_term" label="Title" />
      </v-col>
      <v-col cols="2">
        <v-btn @click="searchPost()" name="submit-btn">Search</v-btn>
      </v-col>
      <v-col cols="2">
        <v-btn name="submit-btn" @click="addPost">Add</v-btn>
      </v-col>
      <v-col cols="2">

        <!-- <template v-slot:activator="{  }"> -->
        <input type="file" ref="file" style="display: none" id="csv_file" name="csv_file" class="form-control"
          @change="loadCSV($event)" />
        <v-btn @click="$refs.file.click()">Upload</v-btn>
        <!-- </template> -->
        <v-dialog v-model="dialog" width="500">



          <v-card>
            <v-card-title class="text-h5 grey lighten-2">
              Privacy Policy
            </v-card-title>

            <v-card-text>
              <v-data-table :headers="csvHeaders" :items="csvDatas" :page.sync="page" hide-default-footer
                @page-count="pageCount = $event" class="elevation-1">\
              </v-data-table>
            </v-card-text>

            <v-divider></v-divider>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" text @click="dialog = false">
                I accept
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>


      </v-col>
      <v-col cols="2">
        <v-btn name="submit-btn">Download</v-btn>
      </v-col>
    </v-row>
    <v-data-table :headers="headers" :items="posts" :page.sync="page" :items-per-page="itemsPerPage" hide-default-footer
      @page-count="pageCount = $event" class="elevation-1">\
      <template v-slot:[`item.title`]="{ item }">
        <nuxt-link :to="`/post/${item.id}/edit`"><a href="#">{{ item.title }}</a></nuxt-link>
      </template>
      <template v-slot:[`item.edit`]="{ item }">
        <nuxt-link :to="`/post/${item.id}/edit`"><a href="#">Edit</a></nuxt-link>
      </template>
      <template v-slot:[`item.delete`]="{ item }">
        <a @click="deletePost(item.id)">Delete</a>
      </template>
    </v-data-table>
    <div class="text-center pt-2">
      <v-pagination v-model="page" :length="pageCount"></v-pagination>
    </div>
  </div>
</template>

<script>
window.axios = require('axios');

export default {

  data() {
    return {
      page: 1,
      pageCount: 0,
      itemsPerPage: 7,
      dialog: false,
      csvDatas: [],
      csvHeaders: [{
        text: 'Post Title', align: 'start',
        sortable: false, value: 'title'
      }, { text: 'Post Description', value: 'description' },],
      headers: [
        {
          text: 'Post Title',
          align: 'start',
          sortable: false,
          value: 'title'
        },
        { text: 'Post Description', value: 'description' },
        { text: 'Posted User', value: 'updated_user_id' },
        { text: 'Posted Date', value: 'created_at' },
        { text: '', value: 'edit' },
        { text: '', value: 'delete' },
      ],
      posts: [],
      search_term: ''
    }
  },
  async asyncData({ $axios, params }) {
    // try {
    // console.log(this.search_term)
    let posts = await $axios.$get(`/posts/`);
    posts.edit = true;
    posts.delete = true;
    return { posts };
  },
  methods: {
    addPost() {
      this.$router.push('/post/post-create');
    },
    async searchPost() {
      console.log(this.search_term)
      let newPosts = await this.$axios.$get(`/posts?search=${this.search_term}`); // get new list of recipes
      this.posts = newPosts;
    },
    async deletePost(post_id) {
      try {
        await this.$axios.$delete(`/posts/${post_id}/`); // delete recipe
        let newPosts = await this.$axios.$get(`/posts/`); // get new list of recipes
        this.posts = newPosts; // update list of recipes
      } catch (e) {
        console.log(e);
      }
    },
    csvJSON(csv) {
      var vm = this
      var lines = csv.split("\n")
      var headers = lines[0].split(",")

      vm.parse_header = lines[0].split(",")
      // lines[0].split(",").forEach(function (key) {
      //   vm.sortOrders[key] = 1
      // })
      const result = []
      lines.map(function (line, indexLine) {
        if (indexLine < 1) return // Jump header line
        var obj = {}
        var currentline = line.split(",")
        headers.forEach((header, indexHeader) => {
          obj[header] = currentline[indexHeader]
        })
        result.push(obj);
      })
      if (result.length > 0) {
        console.log(result)
        this.dialog = true;
        this.csvDatas = result;
      }
      // result.pop() // remove the last item because undefined values
      return result // JavaScript object
    },
    loadCSV(e) {
      var vm = this
      if (window.FileReader) {
        let file = e.target.files[0];
        var reader = new FileReader();
        const xlsxMatch = file.type.match(/^application\/vnd\.openxmlformats-officedocument\.spreadsheetml\.sheet$/gi);
        const csvTsvMatch = file.type.match(/^text\/(csv|tab-separated-values)/gi);

        if (!file || (!xlsxMatch && !csvTsvMatch && !file.name.match(/\.(xlsx|csv)$/gi))) {
          console.error('file name type')
          alert("Canno't read file !");
        } else {
          reader.readAsText(e.target.files[0]);
          
          // Handle errors load
          reader.onload = function (event) {
            console.log('readerrrr', event.target)
            var csv = event.target.result;
                        console.log('--------', csv)

            csv.replace(/^"(.+(?="$))"$/, '$1');
                        console.log('--------', csv)

            vm.parse_csv = vm.csvJSON(csv)
          };
        }


      } else {
        alert('FileReader are not supported in this browser.');
      }
    }
  }
}
</script>

<style scoped>
h1 {
  margin-bottom: 50px;
}

a {
  color: blue;
  text-decoration: underline;
}
</style>