
<template>
  <div class="container">
    <h1>
      Post List
    </h1>
    <v-row>
      <v-col cols="3">
        <v-text-field solo label="Title" />
      </v-col>
      <v-col cols="2">
        <v-btn name="submit-btn">Search</v-btn>
      </v-col>
      <v-col cols="1">
        <v-btn name="submit-btn" @click="addPost">Add</v-btn>
      </v-col>
      <v-col cols="2">
        <v-btn name="submit-btn">Upload</v-btn>
      </v-col>
      <v-col cols="2">
        <v-btn name="submit-btn">Download</v-btn>
      </v-col>
    </v-row>
    <v-data-table :headers="headers" :items="posts" :items-per-page="10" class="elevation-1">\
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
    <!-- <div class="text-center">
      <v-pagination v-model="page" :length="6"></v-pagination>
    </div> -->
  </div>
</template>

<script>
window.axios = require('axios');

export default {

  data() {
    return {
      headers: [
        {
          text: 'Post Title',
          align: 'start',
          sortable: false,
          value: 'title'
        },
        { text: 'Post Description', value: 'description' },
        { text: 'Posted User', value: 'create_user_id' },
        { text: 'Posted Date', value: 'created_at' },
        { text: '', value: 'edit' },
        { text: '', value: 'delete' },
      ],
      posts: []
    }
  },
  async asyncData({ $axios, params }) {
    // try {
    let posts = await $axios.$get(`/posts/`);
    posts.edit = true;
    posts.delete = true;
    return { posts };
  },
  methods: {
    addPost() {
      this.$router.push('/user/post_create');
    },
    async deletePost(post_id) {
      try {
        await this.$axios.$delete(`/posts/${post_id}/`); // delete recipe
        let newRecipes = await this.$axios.$get("/posts/"); // get new list of recipes
        this.posts = newRecipes; // update list of recipes
      } catch (e) {
        console.log(e);
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