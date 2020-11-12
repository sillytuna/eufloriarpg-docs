
DataCan Class
=============



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
* :dn:cls:`Clay.Game.Mod.Entities.DataCan`




Syntax
------

.. code-block:: csharp

    public class DataCan : Entity, IComparable, IAudioSourceInfo, ITargettable





.. dn:class:: Clay.Game.Mod.Entities.DataCan
    :hidden:

.. dn:class:: Clay.Game.Mod.Entities.DataCan


Properties
----------

.. dn:class:: Clay.Game.Mod.Entities.DataCan
    :noindex:
    :hidden:

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.FakePlayerInRange



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool FakePlayerInRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan._activatedSfx



        :rtype: System.String

        .. code-block:: csharp

            public string _activatedSfx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan._closedSfx



        :rtype: System.String

        .. code-block:: csharp

            public string _closedSfx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan._discoveredSfx



        :rtype: System.String

        .. code-block:: csharp

            public string _discoveredSfx { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.activationRange



        :rtype: System.Single

        .. code-block:: csharp

            public static float activationRange { get; set; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.audioRange



        :rtype: UnityEngine.Vector2

        .. code-block:: csharp

            public override Vector2 audioRange { get; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.dataCanID



        :rtype: System.String

        .. code-block:: csharp

            public string dataCanID { get; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.discoveredDataCanCount



        :rtype: System.Int32

        .. code-block:: csharp

            public static int discoveredDataCanCount { get; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.initialDataCanCount



        :rtype: System.Int32

        .. code-block:: csharp

            public static int initialDataCanCount { get; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.isActivated



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isActivated { get; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.isAudioCustomRange



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isAudioCustomRange { get; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.isDiscovered



        :rtype: System.Boolean

        .. code-block:: csharp

            public bool isDiscovered { get; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.isTargetable



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool isTargetable { get; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.modDataCans



        :rtype: System.Collections.Generic.List<System.Collections.Generic.List`1>{System.String<System.String>}

        .. code-block:: csharp

            public static List<string> modDataCans { get; }

    .. dn:property:: Clay.Game.Mod.Entities.DataCan.useSpawnEntityCommand



        :rtype: System.Boolean

        .. code-block:: csharp

            public override bool useSpawnEntityCommand { get; }



Methods
-------

.. dn:class:: Clay.Game.Mod.Entities.DataCan
    :noindex:
    :hidden:

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.Activate(UnityEngine.Vector2, System.String)



        :type atPosition: UnityEngine.Vector2

        :type id: System.String


        .. code-block:: csharp

            public void Activate(Vector2 atPosition, string id)

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.CloneConfiguration(Tuna.Mob)



        :type mob: Tuna.Mob


        .. code-block:: csharp

            public override void CloneConfiguration(Mob mob)

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.EntityFixedUpdate(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void EntityFixedUpdate(float time)

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.GetCommandLine(System.Boolean)



        :type multiLine: System.Boolean

        :rtype: System.String

        .. code-block:: csharp

            public override string GetCommandLine(bool multiLine)

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.GetRespawnString()



        :rtype: System.String

        .. code-block:: csharp

            public override string GetRespawnString()

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.InitialiseApp()




        .. code-block:: csharp

            public static void InitialiseApp()

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.InitialiseLevel()




        .. code-block:: csharp

            public static void InitialiseLevel()

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.InitialiseMod()




        .. code-block:: csharp

            public static void InitialiseMod()

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.ParentColonised()




        .. code-block:: csharp

            public override void ParentColonised()

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.RegisterDataCan(System.String[])



        :type parameters: System.String<System.String>[]


        .. code-block:: csharp

            public static void RegisterDataCan(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.RegisterDataCanLua(System.String)



        :type parameters: System.String


        .. code-block:: csharp

            public static void RegisterDataCanLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.SpawnDataCan(System.String[])



        :type parameters: System.String<System.String>[]

        :rtype: Clay.Game.Mod.Entities.DataCan

        .. code-block:: csharp

            public static DataCan SpawnDataCan(string[] parameters)

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.SpawnDataCanLua(System.String)



        :type parameters: System.String

        :rtype: Clay.Game.Mod.Entities.DataCan

        .. code-block:: csharp

            public static DataCan SpawnDataCanLua(string parameters)

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.Trashed()




        .. code-block:: csharp

            public override void Trashed()

    .. dn:method:: Clay.Game.Mod.Entities.DataCan.Update(System.Single)



        :type time: System.Single


        .. code-block:: csharp

            public override void Update(float time)



