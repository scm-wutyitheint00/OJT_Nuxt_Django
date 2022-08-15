<template>
  <div class="container">
    <h1 class="title">
      Login Form
    </h1>
    <div class="content">
      <form name="contact" action="" method="post">
        <div class="section">
          <label class="form-label" for="name">
            Email:
          </label>
          <input class="form-field" type="email" name="name" id="name" />
        </div>
        <div class="section">
          <label class="form-label" for="email">
            Password:
          </label>
          <input class="form-field" type="password" name="email" id="email" />
        </div>
        <button class="form-button" type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexPage'
}
</script>

<style>
.container {
  margin: 0 auto;
  /* margin-top: 100px; */
  padding: 0 1rem;
  max-width: 1280px;
  text-align: center;
  font-size: 1.3em;
}

label {
  padding: 50px;
}

input {
  padding: 8px;
  width: 400px;
}

.section {
  display: block;
  padding: 10px;
}

button {
  margin-top: 20px;
  padding: 8px 20px 8px 20px;
  font-size: 0.8em;
}
</style>
