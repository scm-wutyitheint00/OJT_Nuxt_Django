<template>
  <div class="container">
    <h1 class="title">
      User Confirm
    </h1>
    <v-form>
      <v-row>
        <v-col cols="2">
          <v-subtitle>Name</v-subtitle>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle">
            {{ $store.state.user.name }}
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subtitle>Email</v-subtitle>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle">
            {{ $store.state.user.email }}
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subtitle>Type</v-subtitle>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle">
            {{ $store.state.user.type }}
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subtitle>Phone</v-subtitle>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle">
            {{ $store.state.user.phone }}
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subtitle>Date of Birth</v-subtitle>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle">
            {{ $store.state.user.dob }}
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subtitle>Address</v-subtitle>
        </v-col>
        <v-col cols="8">
          <p class="text-subtitle">
            {{ $store.state.user.address }}
          </p>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="2">
          <v-subtitle>Profile</v-subtitle>
        </v-col>
        <v-col cols="8">
          <div id="preview">
            <img v-if="url" :src="url" />
          </div>
        </v-col>
      </v-row>
      <v-btn style="margin : 40px 20px" name="submit-btn" @click="submitUser">Create</v-btn>
      <v-btn style="margin : 40px 20px" name="submit-btn" @click="clickCancel">Cancel</v-btn>
    </v-form>
  </div>
</template>

<script>
import validations from '@/utils/validations'
export default {
  created() {
    if (this.$store.state.user.profile) {
      this.url = URL.createObjectURL(this.$store.state.user.profile);
    }
  },
  data() {
    return {
      confirmData: {
        name: this.$store.state.user.name,
        email: this.$store.state.user.email,
        password: this.$store.state.user.password,
        confirmPassword: this.$store.state.user.confirmPassword,
        type: 1,
        phone: this.$store.state.user.phone,
        dob: this.$store.state.user.dob,
        address: this.$store.state.user.address,
        profile: this.$store.state.user.profile
      },
      url: '',
      valid: false,
      ...validations
    }
  },
  methods: {
    clickCancel() {
      this.$router.push('/user/user-create');
    },
    async submitUser() {
      let userData = this.confirmData;
      userData.updated_user_id = 1;
      userData.created_at = new Date().toISOString();
      userData.updated_at = new Date().toISOString();
      const config = {
        headers: { "content-type": "multipart/form-data" }
      };
      let formData = new FormData();
      for (let data in userData) {
        formData.append(data, userData[data]);
        formData.append("file", this.confirmData.profile);
      }
      try {
        this.$axios.$post(`/users/`, formData, config).then(data => {
          console.log(data)
        })
        this.$router.push("/user/");
      } catch (e) {
        console.log(e);
      }
    },
  }
}
</script>

<style>
h1 {
  margin-bottom: 100px;
}

#preview img {
  max-width: 100%;
  max-height: 500px;
}
</style>