
<template>
  <div class="container">
    <h1>
      User List
    </h1>
    <v-row>
      <v-col cols="2.5">
        <v-text-field label="Name" />
      </v-col>
      <v-col cols="2.5">
        <v-text-field label="Email" />
      </v-col>
      <v-col cols="2.5">
        <v-dialog ref="dialog" v-model="searchData.modal" :return-value.sync="date" persistent width="290px">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field v-model="searchData.created_from" label="Created From" prepend-icon="mdi-calendar" readonly
              v-bind="attrs" v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="searchData.created_from" scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="searchData.modal = false">
              Cancel
            </v-btn>
            <v-btn text color="primary" @click="$refs.dialog.save(searchData.created_from)">
              OK
            </v-btn>
          </v-date-picker>
        </v-dialog>
      </v-col>
      <v-col cols="2.5">
        <v-dialog ref="dialog2" v-model="searchData.modal2" :return-value.sync="date" persistent width="290px">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field v-model="searchData.created_to" label="Created To" prepend-icon="mdi-calendar" readonly
              v-bind="attrs" v-on="on"></v-text-field>
          </template>
          <v-date-picker v-model="searchData.created_to" scrollable>
            <v-spacer></v-spacer>
            <v-btn text color="primary" @click="searchData.modal2 = false">
              Cancel
            </v-btn>
            <v-btn text color="primary" @click="$refs.dialog2.save(searchData.created_to)">
              OK
            </v-btn>
          </v-date-picker>
        </v-dialog>
      </v-col>
      <v-col cols="1">
        <v-btn name="submit-btn">Search</v-btn>
      </v-col>
      <v-col cols="1">
        <v-btn name="submit-btn" @click="addUser">Add</v-btn>
      </v-col>
    </v-row>
    <v-data-table :headers="headers" :items="users" :page.sync="page" :items-per-page="itemsPerPage" hide-default-footer
      @page-count="pageCount = $event" class="elevation-1">\
      <template v-slot:[`item.name`]="{ item }">
        <nuxt-link :to="`/user/${item.id}/edit`"><a href="#">{{ item.name }}</a></nuxt-link>
      </template>
      <template v-slot:[`item.email`]="{ item }">
        {{ item.email }}
      </template>
      <template v-slot:[`item.updated_user_id`]="{ item }">
        {{ item.updated_user_id }}
      </template>
      <template v-slot:[`item.phone`]="{ item }">
        {{ item.phone }}
      </template>
      <template v-slot:[`item.dob`]="{ item }">
        {{ item.dob }}
      </template>
      <template v-slot:[`item.address`]="{ item }">
        {{ item.address }}
      </template>
      <template v-slot:[`item.created_at`]="{ item }">
        {{ item.created_at }}
      </template>
      <template v-slot:[`item.updated_at`]="{ item }">
        {{ item.updated_at }}
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
      headers: [
        {
          text: 'Name',
          align: 'start',
          sortable: false,
          value: 'name'
        },
        { text: 'Email', value: 'email' },
        { text: 'Created User', value: 'updated_user_id' },
        { text: 'Phone', value: 'phone' },
        { text: 'Birth Date', value: 'dob' },
        { text: 'Address', value: 'address' },
        { text: 'Created Date', value: 'created_at' },
        { text: 'Updated Date', value: 'updated_at' },
        { text: '', value: 'edit' },
        { text: '', value: 'delete' },
      ],
      users: [],
      searchData: {
        name: '', email: '', created_from: '', created_to: '', menu: false,
        modal: false,
        modal2: false,
        menu2: false,
      }
    }
  },
  async asyncData({ $axios, params }) {
    // try {
    let users = await $axios.$get(`/users/`);
    users.edit = true;
    users.delete = true;
    return { users };
  },
  methods: {
    addUser() {
      this.$router.push('/user/user-create');
    },
    async deletePost(user_id) {
      try {
        await this.$axios.$delete(`/users/${user_id}/`); // delete recipe
        let newRecipes = await this.$axios.$get("/users/"); // get new list of recipes
        this.users = newRecipes; // update list of recipes
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