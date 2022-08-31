<template>
  <div class="container">
    <v-form>
      <v-row>
        <h1 class="title">
          Create User
        </h1>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subtitle>Name</v-subtitle>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.name" label="Name" :rules="[required('name')]" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subtitle>Email Address</v-subtitle>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.email" label="Email" :rules="[required('email'), emailFormat()]"
            type="text" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subtitle>Password</v-subtitle>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.password" label="Password" type="password"
            :rules="[required('password')]" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subtitle>Type</v-subtitle>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-select :items="items" outlined v-model="user.type" :rules="[required('type')]"></v-select>
        </v-col>
      </v-row>

      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subtitle>Phone</v-subtitle>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-text-field outlined v-model="user.phone" label="Phone" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subtitle>Date of Birth</v-subtitle>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-dialog ref="dialog" v-model="user.modal" :return-value.sync="user.dob" persistent width="290px">
            <template v-slot:activator="{ on, attrs }">
              <v-text-field clearable @click:clear="user.dob = null" v-model="user.dob" label="Pick a date"
                prepend-icon="mdi-calendar" readonly v-bind="attrs" v-on="on"></v-text-field>
            </template>
            <v-date-picker v-model="user.dob" scrollable>
              <v-spacer></v-spacer>
              <v-btn text color="primary" @click="user.modal = false">
                Cancel
              </v-btn>
              <v-btn text color="primary" @click="$refs.dialog.save(user.dob)">
                OK
              </v-btn>
            </v-date-picker>
          </v-dialog>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subtitle>Address</v-subtitle>
        </v-col>
        <v-col class="ma-0 pa-3" cols="8">
          <v-textarea outlined v-model="user.address" label="Address" type="text" />
        </v-col>
      </v-row>
      <v-row>
        <v-col class="ma-0 pa-3" cols="2">
          <v-subtitle>Profile</v-subtitle>
        </v-col>
        <v-col class="ma-0 pa-3 text-left" cols="8">
          <input type="file" accept=".jpeg,.jpg,.png,image/jpeg,image/png" aria-label="upload image button"
            @change="selectFile" />

          <div id="preview">
            <img v-if="url" :src="url" />
          </div>
        </v-col>
      </v-row>
      <v-btn name="submit-btn" @click="confirmPost">Confirm</v-btn>
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
  },
  data() {
    return {
      user: {
        name: '',
        email: '',
        password: '',
        confirmPassword: '',
        type: '',
        phone: '',
        dob: '',
        address: '',
        profile: '',
        // type: [admin, user],
        menu: false,
        modal: false,
        menu2: false,
      },
      imageData: '',
      items: ['Admin', 'User'],
      url: '',
      ...validations
    };
  },
  methods: {
    confirmPost() {
      console.log('user', this.user)
      this.$router.push({ path: '/user/user-confirm' });
      this.$store.commit('ADD_USER', this.user)
    },
    clearData() {
      this.user.name = '';
      this.user.email = '';
      this.user.password = '',
        this.user.confirmPassword = '',
        this.user.type = '',
        this.user.phone = '',
        this.user.dob = '',
        this.user.address = '',
        this.user.profile = ''
    },
    async selectFile(e) {
      const file = e.target.files[0];
      if (!file) return;
      this.user.profile = file;
      this.url = URL.createObjectURL(file);
    }
  }
};
</script>

<style scoped>
.col .col-8 {
  padding: 0 !important;
}

.form {
  margin-bottom: 20px;
}

#preview img {
  max-width: 100%;
  max-height: 500px;
}
</style>