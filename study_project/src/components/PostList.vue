<template>
    <div v-if="posts.length > 0">
        <h3>Список постов</h3>
        <transition-group name="post-list">
            <post-item 
                v-for="post in posts" 
                :post="post"
                :curuser="curuser"
                :key="post.id"
                @remove="$emit('remove', post)"
                @openpost="openPost"
            />
        </transition-group>

    </div>
    <h2 v-else style="color: red">
        Список постов пуст
    </h2>
</template>

<script>
import PostItem from '@/components/PostItem';
export default {
    components: { PostItem },
    props: {
        posts: {
            type: Array,
            required: true 
        },
        curuser: String,
    },
    methods: {
        openPost(post) {
            this.$emit('openpost', post);
        }
    }
}
</script>

<style scoped>
.post-list-item {
  display: inline-block;
  margin-right: 10px;
}
.post-list-enter-active,
.post-list-leave-active {
  transition: all 0.4s ease;
}
.post-list-enter-from,
.post-list-leave-to {
  opacity: 0;
  transform: translateX(130px);
}
.post-list-move {
  transition: transform 0.4s ease;
}
</style>