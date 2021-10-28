<template>
    <div class="navbar">
        <h1 style="color: white;">Authors</h1>
        <div class="navbar__btns">
            <div>
                <my-button 
                    class="nav_button" 
                    @click="$emit('articles')"
                >
                    Посты
                </my-button>
                <my-button 
                    class="nav_button"
                    @click="$emit('about')"
                >
                    О сайте
                </my-button>
            </div>
            <div class="userinfo">
                <h3 style="color: white;">Пользователь: {{ activeUser }}</h3>
                <my-button 
                    v-if="activeUser !== 'Anon'"
                    class="nav_button"
                    @click="$emit('exit')"
                >
                    Выход
                </my-button>
            </div>
        </div>
    </div>
</template>

<script>
import MyButton from './UI/MyButton.vue'
export default {
    components: [ MyButton ],
    props: {
        activeUser: String,
    },
    methods: {
  }
    
}
</script>

<style scoped>
.navbar {
    height: 80px;
    background-color: teal;
    box-shadow: 2px 2px 4px gray;
    display: flex;
    flex-direction: column;
}

.nav_button {
    color: white;
    border: 1px solid white;
    padding: 5px 10px;
    align-self: flex-end;
    margin: 0 5px;
}

.userinfo {
    display: flex;
    flex-direction: row;
}
.navbar__btns {
    display: flex;
    justify-content: space-between;
    margin-right: 10px;
}
</style>