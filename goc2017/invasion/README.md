The Nightmare's Observers are on the brink of destruction by an army of undead. The Observers have been sending crows to the masters at the Bastion containing information critical to defeating this army of the dead. Unfortunately, the enemy noticed the reception of these crows, sent his forces to the Bastion and destroyed it.

In the rubble, you've found burnt books, torn scrolls, and smudged handwritten copies of all the messages. Each message was assigned an identifier and stored in triplicate (some master earned his black iron merit badge that day!), so you're sure you have at least one copy of all of the important messages. Sadly however, the order of the messages was lost and some of the messages are completely unrelated!

Luckily you have the identifier of a single message that you know came from the Nightmare's Observers. Can you put together the rest of the messages in order? Humanity is now in your hands. Save Vivinteros by determining the order of the messages sent by the Nightmare's Observers!

### Instructions

Over stdin, you are provided with a JSON-formatted list of all messages received. A message consists of an identifier and a body.

The identifier is a [SHA-256](https://en.wikipedia.org/wiki/SHA-2)-based [HMAC](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code). The HMAC is constructed using the hex-encoded previous message's identifier as the HMAC key, and the [UTF-8](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)-encoded message body as the HMAC message.

In this case, an example message might be:

```
["751e538bf2bc2a0bcdb76f80dc6a9a8baa44b0574814dde49af840054478ada2", "Undead"],
```

The next message might be:

```
["861549981881c60260c6697f068c3d637c356dc01eb855ed456310c188728f17", "hate"],
```

This is a valid next message, because the SHA-256 HMAC of the message `hate` using the key `751e538...` is `8615499...`.

Your input will be a JSON-formatted list of these messages, and your program will receive a command line argument that is the only message identifier you know to be valid and from the Nightmare's Observers.

Your program should output the starting message and all of the messages that follow it in order (UTF-8 encoded).

The output should be in the form of a string containing the message's bodies in the correct order with each word separated by a space (without spaces at the beginning or end).

#### Keep in mind

* The messages are out of order and there may be more than one copy!
* There may even be some unrelated messages.
* There will always be at least one copy of any necessary message.
* Multiple messages may be based off of a previous message!
* There is only one valid message "chain", and the given message identifier will distinguish between multiple message chain forks.

### Example

#### Input

```
./run eac0a2e3d11c82f6ec77e7bfe9f69ad1939e26f564a0d3bc89921b950886c296
```

```
[
  ["9df38df03f2fa666615ae8337ff37b589e8f2b0cfb1359122982b1c1dbd2471b",
   "love"],
  ["7188d84b812e2692a25a5579e9b8bee488f0555b454c56ca4338d6c86d05b57b",
   "hate"],
  ["eac0a2e3d11c82f6ec77e7bfe9f69ad1939e26f564a0d3bc89921b950886c296",
   "Undead"],
  ["e19eace0b3359f43aee2836052c8eb2f6cffed1610a15a57f8970ae659210c21",
   "obsidian!"],
  ["7188d84b812e2692a25a5579e9b8bee488f0555b454c56ca4338d6c86d05b57b",
   "hate"],
  ["e06b63528a69d22a5375bc20c09b8ed82a6a5bb44ff79e77431618e896fe5c2c",
   "hugs!"]
]
```

#### Output

```
Undead hate obsidian!
```
