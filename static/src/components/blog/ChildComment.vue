
<script setup>
import { computed, toRefs } from "@vue/reactivity";

// name: "comment";

const props = defineProps({
    childComment: Object /** @type {Comment} */,
});

const { childComment } = toRefs(props);
</script>

<template>
    <q-item>
        <q-item-section class="">
            {{ childComment.body }}
        </q-item-section>
        <q-item-section side class="">
            <strong>{{ childComment.user.username }}</strong> &bull; 5 min ago
        </q-item-section>
    </q-item>
</template>


<style lang="sass">
.comment-card
    border-left: 2px solid $grey-4
</style>