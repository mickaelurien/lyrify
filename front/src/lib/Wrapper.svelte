<script>
    import { fade } from 'svelte/transition';
</script>

<div class='wrapper' in:fade={{ delay: 400 }} out:fade={{ duration: 400 }}>
    <slot />
</div>

<style>
.wrapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 1rem;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    overflow: hidden;   
}
@media screen and (max-width: 1098px) {
    .wrapper {
        min-width: 90vw;
    }
}
</style>
