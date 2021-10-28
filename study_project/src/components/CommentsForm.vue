<template>
    <form @submit.prevent>
        <my-input 
            v-model="comment.body"
            type="text" 
            placeholder="Комментарий"
        />
        <my-button 
            style="align-self: flex-end;
                   margin-top: 15px"
            @click="createComment"
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
            comment: {
                body: '',
            }
        }
    },
    methods: {
        createComment() {
            this.comment.author = this.curuser;
            this.$emit('create', this.comment);
            this.comment = {
                body: ''
            }
        }
    }
}
</script>

<style scoped>
form {
    display: flex;
    flex-direction: column;
}
</style>