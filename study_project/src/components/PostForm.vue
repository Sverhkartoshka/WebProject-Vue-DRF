<template>
    <form @submit.prevent>
        <h4>Создание поста</h4>
        <my-input 
            v-model="post.title"
            type="text" 
            placeholder="Название"
        />
        <my-input 
            v-model="post.description" 
            type="text" 
            placeholder="Описание"
        />
        <my-input 
            v-model="post.body" 
            type="text" 
            placeholder="Текст"
        />
        <my-button 
            style="align-self: flex-end;
                   margin-top: 15px"
            @click="createPost"
        >
            Создать
        </my-button>
    </form>
</template>

<script>
export default {
    props: {
        curuser: String,
    },
    data() {
        return {
            post: {
                title: '',
                description: '',
                body: '',
            }
        }
    },
    methods: {
        createPost() {
            console.log(this.curuser)
            this.post.id = Date.now();
            this.post.author = this.curuser;
            this.$emit('create', this.post);
            this.post = {
                title: '',
                description: '',
                body: ''
            }
        }
    },
}
</script>

<style scoped>
form {
    display: flex;
    flex-direction: column;
}
</style>
