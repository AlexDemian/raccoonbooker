export function datePickerDateObjectToString (dt) {
    if (!dt) {
        return ''
    }
    let d = dt.singleDate.date
    return `${d.year}-${d.month}-${d.day}`
}