
Stranger Class
==============



Namespace
    :dn:ns:`Clay.Game.Mod.Entities`

Assemblies
    * Clay.Game

----

.. contents::
   :local:



Inheritance Hierarchy
---------------------

* :dn:cls:`System.Object`
* :dn:cls:`Tuna.Mob`
* :dn:cls:`Clay.Game.Mod.Entities.Entity`
* :dn:cls:`Clay.Game.Mod.Entities.Vehicle`
* :dn:cls:`Clay.Game.Mod.Entities.Stranger`




Syntax
------

.. code-block:: csharp

    public class Stranger : Vehicle, IComparable, IAudioSourceInfo, ITargettable, IPathFindingAgent, IStranger





.. dn:class:: Clay.Game.Mod.Entities.Stranger
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.Stranger


Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.Stranger
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.Activate(Attributes, UnityEngine.Vector2, System.Single, Colony, Team)



        :type attr: Attributes

        :type atPosition: UnityEngine.Vector2

        :type atAngle: System.Single

        :type colony: Colony

        :type newTeam: Team


        .. code-block:: csharp

            public override void Activate(Attributes attr, Vector2 atPosition, float atAngle, Colony colony, Team newTeam)

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.ExpireSpeechBubble()




        .. code-block:: csharp

            public void ExpireSpeechBubble()

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.FadeOut()




        .. code-block:: csharp

            public void FadeOut()

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public override string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.GetRespawnString()



        :rtype: System.String

        .. code-block:: csharp

            public override string GetRespawnString()

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.Say(System.String, System.Boolean)



        :type message: System.String

        :type looping: System.Boolean


        .. code-block:: csharp

            public void Say(string message, bool looping = false)

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.SetAiStateMachineState(System.String)



        :type newState: System.String


        .. code-block:: csharp

            public void SetAiStateMachineState(string newState)

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.SpawnStrangerLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.Stranger

        .. code-block:: csharp

            [UsedImplicitly]
            public static Stranger SpawnStrangerLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.StateMachineStateIs(System.String)



        :type state: System.String

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool StateMachineStateIs(string state)

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)

    .. dn:method:: Clay.Game.Mod.Entities.Stranger.UpdateSpeech(Game.Entities.StrangerStages, System.String)



        :type nextStage: Game.Entities.StrangerStages

        :type message: System.String

        :rtype: System.Boolean

        .. code-block:: csharp

            public bool UpdateSpeech(StrangerStages nextStage, string message)



Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.Stranger
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.Stranger.EncounterSeedsReceivedCount



        :rtype: System.Int32

        .. code-block:: csharp

            public int EncounterSeedsReceivedCount { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Stranger.isCurrentEncounterComplete



        :rtype: System.Boolean

        .. code-block:: csharp

            public static bool isCurrentEncounterComplete { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Stranger.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.Stranger.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }



Fields
------

.. dn:class:: Clay.Game.Mod.Entities.Stranger
    :noindex:
    :hidden:

    .. dn:field:: Clay.Game.Mod.Entities.Stranger.s_Encounter



        :rtype: System.Int32

        .. code-block:: csharp

            public static int s_Encounter



