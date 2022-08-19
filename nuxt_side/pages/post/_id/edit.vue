<template>
  <div class="container">
    <h1 class="title">
      Create Post
    </h1>
    <v-form>
      <v-row>
        <v-col cols="2">
          <v-subheader>Title</v-subheader>
        </v-col>
        <v-col cols="8">
          <v-text-field v-model="post.title" label="Title" 
          :rules="[required('title'), minLenght('title', 255)]"
             />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subheader>Description</v-subheader>
        </v-col>
        <v-col cols="8">
          <v-textarea v-model="post.description" label="Description" 
          :rules="[required('description')]"
        type="text" />
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subheader>Status</v-subheader>
        </v-col>
        <v-col cols="8">
          <v-checkbox
              v-model="ex4"
              color="info"
              value="info"
              hide-details
            ></v-checkbox>
        </v-col>
      </v-row>
      
      <v-btn name="submit-btn" @click="submitPost">Confirm</v-btn>
      <v-btn name="submit-btn" @click="clearData">Clear</v-btn>
    </v-form>
  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {
  head() {
    return {
      title: "View Post"
    };
  },
  async asyncData({ $axios, params }) {
    try {
      let post = await $axios.$get(`/posts/${params.id}`);
      return { post };
    } catch (e) {
      return { post: [] };
    }
  },
  data() {
    return {
      post: {
        name: "",
        picture: "",
        ingredients: "",
        difficulty: "",
        prep_time: null,
        prep_guide: ""
      },
      ...validations
    };
  },
   methods: {
    async submitPost() {
      let editedpost = this.post
   
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in editedpost) {
        formData.append(data, editedpost[data]);
      }
      try {
        let response = await this.$axios.$patch(`/posts/${editedpost.id}/`, formData, config);
        this.$router.push("/post/");
      } catch (e) {
        console.log(e);
      }
    },
    clearData() {
      this.post.title = '';
      this.post.description = '';
    }
  }
};
</script>

<style scoped>
</style>