export function useTextFormat() {

    const cut = (text: string, finalLen: number): string => {
        return text.slice(0, finalLen - 3) + '...'
    }

    return {
        cut,
    }
}