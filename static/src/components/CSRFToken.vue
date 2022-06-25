<template>
    <input
        name="csrfmiddlewaretoken"
        type="hidden"
        :value="$q.cookies.get('csrftoken')"
    />
</template>

<script>
export default {};
</script>

<style>
</style>