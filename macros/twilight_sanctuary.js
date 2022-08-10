// name: Twilight Sanctuary
// img: icons/magic/life/cross-embers-glow-yellow-purple.webp

async function tempHP({actor}) {
  const clericStats = character.data.items.getName("Cleric");
  const clericLvl = clericStats.data.data.levels;
  const target = actor.name;
  const currentTHP = actor.data.data.attributes.hp.temp;
  const newTHP = new Roll("1d6 + @level", {level : clericLvl});
  let output;
  await newTHP.roll();
  try {
    game.dice3d.showForRoll(newTHP);
  } catch {
  }
  if (newTHP.total > currentTHP) {
    output = "<b>" + target + "</b> is raised to " + newTHP.total + " temp HP.";
    actor.data.data.attributes.hp.temp = newTHP.total;
  } else {
    output = "<b>" + target + "</b> already has more than " + newTHP.total +
             " temp HP.";
  }
  let tooltip = await newTHP.render();
  output += tooltip;
  return output;
}

if (token) {
  output = await tempHP({actor : token.actor});
  msg =
      "<h2>Sanctuary of the Glade</h2> Memories of twilight in the Glade imbue the party with resolve...<br><br>" +
      output;
  ChatMessage.create({
    content : msg,
  });
}