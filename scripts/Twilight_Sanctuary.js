async function tempHP({
    actor
}) {
    let target = actor.name;
    let currentTHP = actor.data.data.attributes.hp.temp;
    let newTHP = new Roll("1d6 + @level", {
        level: 2
    });
    let output;
    await newTHP.roll();
    game.dice3d.showForRoll(newTHP);
    if (newTHP.total > currentTHP) {
        output = "<b>" + target + "</b> is raised to " + newTHP.total + " temp HP.";
        actor.data.data.attributes.hp.temp = newTHP.total;
    } else {
        output = "<b>" + target + "</b> already has more than " + newTHP.total + " temp HP.";
    }
    return output;
}

if (token) {
    output = await tempHP({
        actor: token.actor
    });
    msg = "<h2>Sanctuary of the Glade</h2> Memories of twilight in the Glade imbue the party with resolve...<br><br>" + output;
    ChatMessage.create({
        content: msg,
    });
}